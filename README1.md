# Intial Design Doc for Project

## Crypto Bot Design Doc

## Bot logic/ Flow

### Market Monitoring, Data Retrieval for Analysis

Every 5-15 minutes we want to fetch data from the Coinbase API for mid-frequency trading, once the data has been retrieved we pass it to technical indicators. Technical indicators will be fed into a scoring system that combines multiple indicators to generate signals. We could also potentially include volume analysis to validate and verify a strong movement. 

### Signal Validation, Order Execution

Once a signal has been identified and validated, a minimum confidence threshold must be met to prevent false signals. Then pre-trade checks will be executed such as current volatility, and tradable account balance set by the user. The order execution system will attempt to execute the order, if the order is not successful, retry logic will be ran, if after a certain number of attempts the order is not executed, the attempt will be canceled. When the order is executed successfully, it is written to a log with all the orders data. 

### Position Management, Exit Strategy

We will use trailing stop-loss mechanisms to monitor the position and prevent any extreme loss. The bot will exit when a take-profit level has been met. Position monitoring system will be more active than entry monitoring system. Partial exit strategies will be considered if take-profit levels are not met after a period of time. Create logic for conditions of running profit and emergency exit scenarios. On successful exit write to the log to keep track of trades. 

### Risk Management, Portfolio Balancing Act

Pre-trade position sizing should be set within a variation of a certain percent provided by the user. This will create a account separation of active vs inactive balance. Create daily loss limits on which the bot should stop trading for the day.

### System Reliability

Comprehensive error handling, ability to push to user that something has gone wrong with the bot. Automated alerts for critical situations. System state persistence in case of need for restart. 

# Key goals for bot

- High efficiency, not too resource intensive
- Simplicity, ease of use should be a top priority
- Robust and intelligent
- High reliability and consistency
- Architecture of bot would be executed through multiple threads
