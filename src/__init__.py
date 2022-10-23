from src.steps.process_market import ProcessMarketDemo



def main():
  demoMarket = ProcessMarketDemo()
  demoMarket.auth()
  demoMarket.add_item_cart()
  demoMarket.handle()