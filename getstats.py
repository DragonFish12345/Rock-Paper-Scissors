import json

# Getting Stats

fin = open('stats.json')
wins, ties, losses = fin.read().splitlines()


def get_wins():
    return wins


def get_ties():
    return ties


def get_losses():
    return losses


