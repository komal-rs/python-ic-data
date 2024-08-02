from google.cloud import bigquery
from google.oauth2 import service_account
import os
import json
import requests
from datetime import datetime, timedelta
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import encode, decode, Types
from ic.canister import Canister
import ssl


if __name__ == "__main__":

    # getting SSL error
    # canisters_list = get_canisters_list()
    # print(canisters_list)

    # read canisters.txt as json and get json["targets"] to get canister_list
    # with open("canisters.txt", "r") as file:
    #     canisters_list = json.load(file)[0]["targets"]

    iden = Identity()
    client = Client(
        url="https://ic0.app"
    )  # replace with https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.ic0.app/ for mainnet
    agent = Agent(iden, client)

    ind_canister_did = open("individual_canister.did").read()
    # for canister_id in canisters_list[:1]:
    # try:
    # canister_id = canister_id.split(".")[0]
    canister_id = "fa3k7-syaaa-aaaap-qcnoq-cai"
    # canister = Canister(agent=agent, canister_id=canister_id, candid=ind_canister_did)
    # print(canister_id)
    # res = canister.get_posts_of_this_user_profile_with_pagination_cursor(0, 10)
    # print(res)
    # print()

    # params = [
    #     {"type": Types.Nat64, "value": 0},
    #     {"type": Types.Nat64, "value": 10},
    # ]
    res = agent.query_raw(
        canister_id,
        "get_watch_history",
        encode([]),
    )
    print(res)
    print()
    # except Exception as e:
    #     print(e)

    # cnt = 0

    # for row in results:
    #     # print(dict(row))

    #     result = canister.insert(
    #         "col1",
    #         [row["ml_generate_embedding_result"]],
    #         [row["uri"]],
    #     )

    #     cnt += 1
    #     # if cnt % 10 == 0:
    #     print(cnt, row["uri"], result)
    #     break
