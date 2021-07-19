# ShareBot
Telegram bot to easily manage shared expenses. Written using Aiogram library, MongoDB was used as a database.

Bot: [@shareyourcostsbot](https://t.me/shareyourcostsbot)
## Description
To get all available commands enter `/help` in chat with bot

#### Groups commands (these commands work only in groups):
 * `/manage_cards` - opens cards window, use to add your cards and see other people's cards
 * `/create_purchase` - use to add purchase
 * `/create_purchase <cost> <title>` - to do it quicker
 * `/get_all_purchases` - use to get all purchases in this group
#### Both groups and private chat:
 * `/add_card` - use to add card
 * `/add_card <card_number> <bank_name>(optional)` - to do it quicker

### Purchase window  
After creating each purchase will have 4 buttons: `Join as buyer`, `Join as payer`, `Calculate`, `Delete purchase`  
 * If you contributed part of the money to the purchase press `Join as buyer` and bot will ask you how much did you pay. After that you will see yourself in buyers list with amount of money you spent. If you enter wrong value you will have to press the button again. You can press again to remove yourself from the list.  
 * If you are one of those who will pay for this purchase press `Join as payer` and you will see yourself in payers list. You can press again to remove yourself from the list.  
 * If you want to delete purchase press `Delete purchase`. Please note you can't cancel this operation.
 * If all payers and buyers have joined press `Calculate` and the bill will be sent in a new message. It will look as following:  
```
Result:
   User1 10  
   User2 10  
   User3 -20  
```  
Postitive amount to the right of name means that this person have to give this amount of money  
Negative - this person have to receive this amount of money  
Also you can receive next warnings:  
`Take into account that buyers field is empty, something may be wrong!`  
`Please be aware that total cost of the purchase is different from the amount of money that buyers paid!`  
The calculation will be done anyway.  

### Cards window  
Opens with `/manage_cards` command.  
Cards window has 2 buttons: `Edit cards`, `Add youself`.  
 * `Add yourself` works exactly like `/add_card` command. It is just another way to add your card.
 * `Edit cards` will redirect you to the window for selecting the user to be edited. You can add and delete user cards. Please note that anyone can add you a card or delete existing using this window, so be aware of unscrupulous colleagues😅

### All purchases window  
Opens with `/get_all_purchases` command.  
If group has any purchases they will be listed as buttons. Each button gives a purchase window (in a new message).  

### Important info  
When you call commands or press buttons that are waiting for your response (e.g. when you join as buyer and enter amount of money that you have paid) you will have only 15 seconds to answer so that everything works correctly. If you miss it the message which refers to this call won't be edited and you may think that nothing happened. It happens because of Telegram feature of generating callback data for buttons. Try to reload window by pressing other buttons (e.g. for purchase window double click `Join as payer`, for cards window click `Edit cards` and then `Back to users`).  
  
## Authors
 * [Ivan Shkvir](https://github.com/IvanShkvir)  
 * [Nazar Kohut](https://github.com/nazarkohut)  
 * [Nazar Furdychka](https://github.com/nazfurdychka)  
