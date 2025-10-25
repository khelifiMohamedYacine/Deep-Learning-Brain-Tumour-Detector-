# main.py

from src.train import train_model
from src.evaluate import evaluate_model

def main():
    # Train the model
    train_model()

    # Evaluate the model after training
    evaluate_model()

if __name__ == '__main__':
    main()
