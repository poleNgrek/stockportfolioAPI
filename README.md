# stockportfolioAPI


### The task 🧩

The aim of the code is to build a very simple API, which mimics a basic stock portfolio manager. It is comprised of
financial instrument records and a simple portfolio object used as a means to track buy-sell events (trades) of desired
instruments/stocks, the current holding value and the profit-loss of all buy-sell events.

#### Technologies Used 🧱

* Docker
* Django
* Postgres
* GraphQL

#### Specifications 📘
* There are three models:
  * An Instrument model: `trading.models.Instruments`
    The attributes for this model are: id, name, symbol, date, isEnabled, type, iexId
  * A Portfolio model: `trading.models.Portfolios`
    The attributes for this model are: id, name, description, holding_value, total_profit_loss, created_at, last_modified
  * A Trade model: `trading.models.Trades`
    The attributes for this model are: id, instrument, portfolio, volume, buy_value, sell_value, profit_loss, created_at, last_modified
* There is no authorization and accounts, it is just a simple open API. However, the models are registered in the admin,
so if you want, you can create an admin user account and access them at *http://localhost:8000/admin/*. This way, you can add mock-up data using a graphical environment.
* The code exposes a GraphQL API(graphene-django) for:
  1. Fetching instrument data
  2. Fetching portfolio details
  3. Editing a portfolios's attributes
  4. Editing a trade's attributes
  5. Creating a trade
  6. Creating a portfolio
  7. A search function for instruments that filters based on id,name or symbol


### Instructions ⏳

- **install docker and docker-compose**.
- **Clone the project**.
- **Navigate to the root file**. 
- **Open a command line and type `docker-compose up`**. 
- **Navigate to** _(http://localhost:8000/graphql)_

#### Testing ⚙️
- The testing is somewhat limited and incomplete at the moment. However there are some basic testing files for models, for a resolve and for  testing the database connection. You can run the tests by opening another shell and typing, for example, `docker-compose run web python manage.py test trading.tests.commands` or if you want to test the models just replace the word commands with models.

#### The docker-compose file ⚠️
- The docker-compose file creates two services. The db service downloads a postgres image, gives it a volume and sets the necessary environment variables. The web service depends on the db service and runs after the database connection has been established. The service checks before running, through a custom command, that the database is connected, migrates the models, imports the json instrument data and finally runs the server. The most important environment variables are set here to avoid touching the database variables directly from settings.py.

### The imported data ✅

the instrument data provided in json format (derived from https://api.iextrading.com/1.0/ref-data/symbols)

### Need help? 🤯

Please contact me and I will try to answer as soon as possible. 
