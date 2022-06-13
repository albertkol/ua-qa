# UA QA Tool

## How to install?

`ua-contracts` is a private repo. So in order to fetch the binary, tool will use try to make use of your github ssh key to clone the repo. 

Running the app steps:
```bash
scripts/build
scripts/run
```

Alternatively you can always manually clone and install the `ua-contracts` binary:
```bash 
Build ua-contracts
sudo snap install go  # You will need to install go
git clone git@github.com:canonical/ua-contracts.git  # Clone the repo 
cd ua-contracts 
(optional) set GOPATH and add GOPATH to PATH
make install
```

```bash
Run ua-qa
git clone git@github.com:albertkol/ua-qa.git
python3 src/app.py
```

## How to use ua-qa?

`ua-qa` has the following commands:
- `login` - to login with you SSO account, you need premissions to use it
- `status` - to get the current state of the app; the app stores some values like `email`, `account_id` for quick use
- `use` - to set the user you wish to work on; the purchase account of the user with the email address provided will automatically be set in the state. If user has no purchase account you will be prompted to initialise it, but you don't have to
- `attach offer` - attaches an offer to the user that is in `use`; user must have a purchase account
- `attach offer --multi` - attaches a multiple products offer to the user that is in `use`, user must have a purchase account
- `attach renewal` - attaches a renewal to the user that is in `use`; user must *not* have a purchase account
- `attach renewal --multiple` - attaches a multiple products renewal to the user that is in `use`; user must *not* have a purchase account
- `attach renewal --expired` - attaches an expired renewal to the user that is in `use`; user must *not* have a purchase account
- `attach renewal --no-actionable` - attaches a big renewal, making it not actionable, to the user that is in `use`; user must *not* have a purchase account
- `clear` - detaches the current purchase account from the user in `use`
- `exit` - finish ua-qa
