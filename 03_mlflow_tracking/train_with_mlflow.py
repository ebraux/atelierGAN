
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Reshape, LeakyReLU
from tensorflow.keras.models import Sequential
import numpy as np
import mlflow
import mlflow.tensorflow
import os

# === Configuration ===
BUFFER_SIZE = 60000
BATCH_SIZE = 128
LATENT_DIM = 100
EPOCHS = 50

# === Données MNIST ===
(x_train, _), (_, _) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_train = x_train.reshape(-1, 28*28)
train_dataset = tf.data.Dataset.from_tensor_slices(x_train).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

# === Modèles ===
def build_generator():
    return Sequential([
        Dense(128, input_shape=(LATENT_DIM,), activation=LeakyReLU(0.2)),
        Dense(784, activation='sigmoid'),
        Reshape((28, 28))
    ])

def build_discriminator():
    return Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(128, activation=LeakyReLU(0.2)),
        Dense(1, activation='sigmoid')
    ])

# === Fonction de perte et optimisateurs ===
cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=False)
generator = build_generator()
discriminator = build_discriminator()
generator_optimizer = tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.Adam(1e-4)

# === Fonction d'entraînement ===
@tf.function
def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, LATENT_DIM])
    with tf.GradientTape() as disc_tape, tf.GradientTape() as gen_tape:
        generated_images = generator(noise, training=True)
        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)
        disc_loss = cross_entropy(tf.ones_like(real_output), real_output) + \
                    cross_entropy(tf.zeros_like(fake_output), fake_output)
        gen_loss = cross_entropy(tf.ones_like(fake_output), fake_output)
    gradients_d = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    gradients_g = gen_tape.gradient(gen_loss, generator.trainable_variables)
    discriminator_optimizer.apply_gradients(zip(gradients_d, discriminator.trainable_variables))
    generator_optimizer.apply_gradients(zip(gradients_g, generator.trainable_variables))
    return gen_loss, disc_loss

# === Entraînement avec MLflow ===
def train(dataset, epochs):
    gen_losses, disc_losses = [], []

    mlflow.set_experiment("MNIST_GAN_TF_Terminal")
    with mlflow.start_run():
        mlflow.log_params({
            "epochs": epochs,
            "batch_size": BATCH_SIZE,
            "latent_dim": LATENT_DIM
        })

        for epoch in range(epochs):
            gen_total, disc_total, steps = 0, 0, 0
            for batch in dataset:
                g_loss, d_loss = train_step(batch)
                gen_total += g_loss
                disc_total += d_loss
                steps += 1
            gen_avg = gen_total / steps
            disc_avg = disc_total / steps
            gen_losses.append(gen_avg.numpy())
            disc_losses.append(disc_avg.numpy())

            mlflow.log_metric("generator_loss", gen_avg.numpy(), step=epoch)
            mlflow.log_metric("discriminator_loss", disc_avg.numpy(), step=epoch)
            print(f"Epoch {epoch}: G_loss={gen_avg:.4f}, D_loss={disc_avg:.4f}")

        # Enregistrer le modèle du générateur
        tf.saved_model.save(generator, "exported_generator")
        mlflow.tensorflow.log_model(tf_saved_model_dir="exported_generator", tf_meta_graph_tags=None, tf_signature_def_key=None, artifact_path="generator_model")

if __name__ == "__main__":
    train(train_dataset, EPOCHS)
