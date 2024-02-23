#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 01:50:06 2023

@author: costantino_ai
"""

from copy import deepcopy
import os
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

def train_model_on_mnist(
    untrained_model,
    data_loader,
    checkpoint_path="./model/alexnet_mnist.pth",
    epochs=20,
    learning_rate=0.001,
    device="cpu",
):
    """
    Train a model on the MNIST dataset with checkpointing, device handling, and logging.

    This function takes an untrained PyTorch model, a data loader for the MNIST dataset, and various training
    configuration parameters. It trains the model, saves checkpoints during training, and returns the trained model.

    :param untrained_model: Model to be trained.
    :type untrained_model: torch.nn.Module
    :param data_loader: DataLoader for MNIST.
    :type data_loader: torch.utils.data.DataLoader
    :param checkpoint_path: Path for saving the model checkpoint (default is "./model/alexnet_mnist.pth").
    :type checkpoint_path: str
    :param epochs: Number of training epochs (default is 20).
    :type epochs: int
    :param learning_rate: Learning rate for the optimizer (default is 0.001).
    :type learning_rate: float
    :param device: Device to use for training ('cpu' or 'cuda') (default is "cpu").
    :type device: str
    :return: Trained model.
    :rtype: torch.nn.Module

    :Example:

    >>> import torch
    >>> from torchvision import datasets, transforms
    >>> from torch.utils.data import DataLoader
    >>> import torchvision.models as models
    >>>
    >>> # Define a sample untrained model
    >>> model = models.AlexNet()
    >>>
    >>> # Define a data loader for MNIST (example, actual data loader setup may differ)
    >>> transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    >>> mnist_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
    >>> mnist_dataloader = DataLoader(mnist_dataset, batch_size=64, shuffle=True)
    >>>
    >>> # Train the model
    >>> trained_model = train_model_on_mnist(model, mnist_dataloader, epochs=5)
    """
    # Ensure checkpoint directory exists
    os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
    model = deepcopy(untrained_model)

    # Check for a checkpoint
    if os.path.isfile(checkpoint_path):
        print("Loading checkpoint...")
        model_dict = torch.load(checkpoint_path, map_location=device)
        model.load_state_dict(model_dict, strict=False)
    else:
        print("Checkpoint not found, starting training...")
        # Deep copy to keep the original model unmodified
        model.to(device)  # Move model to the specified device
        model.train()

        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)

        # Initialize lists for plotting
        plot_loss = []
        plot_accuracy = []

        for epoch in range(epochs):
            running_loss = 0.0
            correct = 0
            total = 0

            for i, (inputs, labels) in enumerate(
                tqdm(data_loader, desc=f"Epoch {epoch + 1}/{epochs}"), 0
            ):
                inputs, labels = inputs.to(device), labels.to(device)  # Move data to device

                optimizer.zero_grad()  # Zero the parameter gradients

                # Forward pass, backward pass, and optimize
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                # Update running loss and accuracy
                running_loss += loss.item()
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

                # Print statistics every 10 batches
                if (i + 1) % 100 == 0:
                    print(
                        f"Batch {i + 1}, Loss: {running_loss / (i + 1):.4f}, Accuracy: {100 * correct / total:.2f}%"
                    )

            # Store loss and accuracy for plotting
            epoch_loss = running_loss / len(data_loader)
            epoch_acc = 100 * correct / total
            plot_loss.append(epoch_loss)
            plot_accuracy.append(epoch_acc)

            print(f"Epoch {epoch + 1}/{epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.2f}%")

        print("Training complete, saving model...")
        model.eval()
        torch.save(model.state_dict(), checkpoint_path)

        # Plotting loss and accuracy
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.plot(plot_loss, label="Loss")
        plt.title("Training Loss")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.subplot(1, 2, 2)
        plt.plot(plot_accuracy, label="Accuracy")
        plt.title("Training Accuracy")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy")
        plt.show()

    return model