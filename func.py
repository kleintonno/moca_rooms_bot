from ens import ENS
import requests
import web3
from config import infura_url, subgraph_url
from eth_utils import from_wei
from web3 import Web3
from query import query
w3 = Web3(web3.HTTPProvider(infura_url))
ns = ENS.fromWeb3(w3)


# function to use requests.post to make an API call to the subgraph url
def try_to_resolve_ens(address):
    domain = ns.name(address)
    if domain is None:
        return address
    else:
        return domain


def run_query(q):
    request = requests.post(subgraph_url
                            ,
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.      {}'.format(request.status_code, query))


def get_data():
    result = run_query(query)
    auction = result['data']['auctions']
    amount = str(from_wei(int(auction[0]['bids'][0]['amount']), 'ether'))
    last_auction_data = {
        "id": auction[0]['id'],
        "size": auction[0]['floor']['size'],
        "endTime": auction[0]['endTime'],
        "bidder": try_to_resolve_ens(str(auction[0]['bids'][0]['bidder'])),
        "bid_id": auction[0]['bids'][0]['id'],
        "memberspass": f"http://app.museumofcryptoart.com/member/{auction[0]['bids'][0]['bidder']}",
        "amount": amount
    }
    return last_auction_data
