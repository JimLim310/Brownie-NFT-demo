from brownie import AdvancedCollectible, account
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3


def create_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address, amount=Web3.toWei(0.25, "ether"))
    creation_tx = advanced_collectible.createCollectible({"from": account})
    creation_tx.wait(1)
    print("Collectible created!")


def main():
    create_collectible()
