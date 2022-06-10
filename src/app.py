from datetime import datetime, timedelta
import os

import yaml
from more_itertools import first

from config import (
    CBLUE,
    CEND,
    CGREEN,
    CGREY,
    COMMANDS,
    CONTRACTS_BIN,
    CRED,
    CYELLOW,
    TITLE,
)
from helpers import get_payload

print(TITLE)

marketplace = "canonical-ua"
email = ""
account_id = ""
subcription_id = ""
contract_id = ""

while True:
    command = input(f"{CYELLOW}ua-qa [{email}] > {CEND}").lower()

    # if empty
    if not command:
        continue

    # if command is invalid
    elif command not in COMMANDS:
        print(f"{CRED}Error: Invalid command{CEND}")
        continue

    # login command
    elif command == "login":
        os.system(f"{CONTRACTS_BIN} login")
        os.system(f"{CONTRACTS_BIN} call get-user-info")
        os.system(f"{CONTRACTS_BIN} call get-accounts")

    # status command
    elif command == "status":
        print("Environment variables:")
        print(f"- marketplace: {CGREY}{marketplace}{CEND}")
        print(f"- email: {CGREY}{email}{CEND}")
        print(f"- account: {CGREY}{account_id}{CEND}")
        print(f"- subcription: {CGREY}{subcription_id}{CEND}")
        print(f"- contract: {CGREY}{contract_id}{CEND}")

    # use command
    elif command == "use":
        account_id = ""
        subcription_id = ""
        contract_id = ""

        email = input(f"{CBLUE}Email: {CEND}").lower()

        if not email:
            print(f"{CRED}Error: Invalid email{CEND}")
            continue

        get_accounts_by_email = (
            f"{CONTRACTS_BIN} call get-accounts --email={email}"
        )

        raw_accounts = os.popen(get_accounts_by_email).read()
        accounts = yaml.safe_load(raw_accounts).get("accounts")

        if not accounts:
            print(f"{CRED}Error: No accounts found{CEND}")

        account_id = first(
            [
                account.get("id")
                for account in accounts
                if account.get("type") == "paid"
            ],
            default="",
        )

        if account_id:
            print(f"{CGREEN}Set account: {account_id}{CEND}")

            continue

        # Init Purchase account
        print(f"{CRED}Error: User has no purchase account{CEND}")

        should_init_account = input(
            f"Init purchase account? (yes/no): {CEND}"
        ).lower()

        if should_init_account[0] != "y":
            print(f"Purchase account was not initialised{CRED}")

            continue

        ensure_account = get_payload(
            payload="ensure_account",
            replaces={"email": email},
        )

        ensure_account_command = (
            f"echo '{ensure_account}' | "
            f"{CONTRACTS_BIN} call "
            f"EnsureAccountForMarketplace {marketplace} -"
        )

        raw_account = os.popen(ensure_account_command).read()
        print(f"{CGREEN}Purchase account was initialised{CEND}")

        account_id = yaml.safe_load(raw_account).get("accountID")
        print(f"{CGREEN}Set account: {account_id}{CEND}")

    # attach renewal command
    elif "attach renewal" in command:
        if not email:
            print(f"{CRED}Error: Set user with `use` command{CEND}")

            continue

        if account_id:
            print(
                f"{CRED}Error: Cannot attach renewals to user with account. "
                f"Use `clear` command to remove account{CEND}"
            )

            continue

        contract_start = ""
        contract_end = ""
        contract_start_2 = ""
        contract_end_2 = ""
        renewal_start = ""
        renewal_end = ""
        renewal_start_2 = ""
        renewal_end_2 = ""

        format_now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        random_account_id = f"ua_qa_account_{format_now}"
        random_asset_id = f"ua_qa_asset_{format_now}"
        random_asset_id_2 = ""

        date = datetime.today() - timedelta(days=180)
        contract_start = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        date = datetime.today() + timedelta(days=180)
        contract_end = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        date = datetime.today() - timedelta(days=90)
        renewal_start = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        date = datetime.today() + timedelta(days=90)
        renewal_end = date.strftime("%Y-%m-%dT%H:%M:%SZ")

        payload = ""
        if "--expired" in command:
            payload = "renewal-expired"
            date = datetime.today() - timedelta(days=800)
            contract_start = date.strftime("%Y-%m-%dT%H:%M:%SZ")
            date = datetime.today() + timedelta(days=500)
            contract_end = date.strftime("%Y-%m-%dT%H:%M:%SZ")
            date = datetime.today() - timedelta(days=410)
            renewal_start = date.strftime("%Y-%m-%dT%H:%M:%SZ")
            date = datetime.today() + timedelta(days=590)
            renewal_end = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif "--multi" in command:
            payload = "renewal-multi"
            random_asset_id_2 = f"{random_asset_id}2"
            date = datetime.today() - timedelta(days=150)
            contract_start_2 = date.strftime("%Y-%m-%dT%H:%M:%SZ")
            date = datetime.today() + timedelta(days=210)
            contract_end_2 = date.strftime("%Y-%m-%dT%H:%M:%SZ")
            date = datetime.today() - timedelta(days=60)
            renewal_start_2 = date.strftime("%Y-%m-%dT%H:%M:%SZ")
            date = datetime.today() + timedelta(days=120)
            renewal_end_2 = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif "--no-actionable" in command:
            payload = "renewal-no-action"
        else:
            payload = "renewal"

        renewal = get_payload(
            payload=payload,
            replaces={
                "random_account_id": random_account_id,
                "random_asset_id": random_asset_id,
                "random_asset_id_2": random_asset_id_2,
                "contract_start": contract_start,
                "contract_end": contract_end,
                "contract_start_2": contract_start_2,
                "contract_end_2": contract_end_2,
                "renewal_start": renewal_start,
                "renewal_end": renewal_end,
                "renewal_start_2": renewal_start_2,
                "renewal_end_2": renewal_end_2,
            },
        )

        renewal_command = (
            f'echo "{renewal}" | '
            f"{CONTRACTS_BIN} call EnsureContractForExternalAccount "
            f"{random_account_id} -"
        )

        raw_renewal = os.popen(renewal_command).read()
        print(raw_renewal)

        account_id = yaml.safe_load(raw_renewal).get("accountInfo").get("id")
        print(f"{CGREEN}Set account: {account_id}{CEND}")

        premission_payload = {"email": email, "role": "admin"}

        permission_command = (
            f'echo "{premission_payload}" | '
            f"{CONTRACTS_BIN} call "
            f"SetAccountUserRole {account_id} -"
        )

        raw_permission = os.popen(permission_command).read()
        print(raw_permission)

        print(f"{CGREEN}Renewal was attached{CEND}")

    # attach offer command
    elif "attach offer" in command:
        if not email or not account_id:
            print(f"{CRED}Error: Set user with `use` command{CEND}")

            continue

        payload = "offer-multi" if "--multi" in command else "offer"
        offer = get_payload(
            payload=payload,
            replaces={"account_id": account_id},
        )

        offer_command = (
            f"echo '{offer}' | "
            f"{CONTRACTS_BIN} call "
            f"EnsureOffer {marketplace} -"
        )

        raw_offer = os.popen(offer_command).read()
        print(raw_offer)
        print(f"{CGREEN}Offer was attached{CEND}")

    # clear command
    elif command == "clear":
        are_you_sure = input(
            f"Are you sure you want to clear account? (yes/no): {CEND}"
        ).lower()

        if are_you_sure[0] == "y":
            clear_account = (
                f"{CONTRACTS_BIN} set-account-access "
                f"{account_id} none {email} --force"
            )
            os.system(clear_account)
            account_id = ""

    # exit command
    elif command == "exit":
        print(f"{CGREEN}Goodbye!{CEND}")
        break
