A CLI tool to manage your gandi.net domains

## Usage

* To install, `git clone && cd gandi-cli` followed by `pip install .`

* Run `gandi` to get an overview of available options and commands.
  A user API key and the hostname to use are required options, they
  can be passed via command line options or in environment variables.

## Configuration

Some options can be configured via environment variables:

### GANDI_API_KEY

Your API key

### GANDI_API_URL

At time of writing:

* The test server is `https://rpc.ote.gandi.net/xmlrpc/`
* The production server is `https://rpc.gandi.net/xmlrpc/`

For more info please refer to the
[API Overview](http://doc.rpc.gandi.net/overview.html#introduction).

### Links

* http://doc.rpc.gandi.net/domain/usage.html
