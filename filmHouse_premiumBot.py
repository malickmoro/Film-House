from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.ext import JobQueue, CallbackContext
from config import TOKEN

#FIREBASE
# # Firebase Admin initialization
# cred = credentials.Certificate(FIREBASE_KEY_PATH)
# firebase_admin.initialize_app(cred)
# db = firestore.client()

#COMMANDS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ensure update.message is not None before proceeding
    if update.message:
        # Define the new keyboard layout
        keyboard = [
            ['Subscription Plans', 'Subscription Status'],  # Row 1 with two buttons
            ['FAQs', 'Help and Support']  # Row 2 with two buttons
        ]
        # Create a reply markup with the keyboard layout
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

        # Get the user's first name to personalize the greeting, fallback to username if not available
        user = update.message.from_user
        user_first_name = user.first_name if user and user.first_name else "there"

        # Update the message text to include the user's name
        message = (f"Hey {user_first_name}!,\n"
                   "My name is Kevin Hart.\n"
                   "Select what you'd like to do today from the options below:")

        # Send a message with the reply keyboard markup
        await update.message.reply_text(text=message, reply_markup=reply_markup, parse_mode="HTML")
    else:
        # Handle case where update.message is None
        print("Received an update without a message.")


async def subscription_plans(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if update.message is not None
    if update.message:
        buttons = [
            [InlineKeyboardButton("Monthly Chill GHC 10.00", callback_data= "monthly")], 
            [InlineKeyboardButton("Yearly Chill GHC 100.00", callback_data= "yearly")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        message = ("Film House Premium\n"
                   "---------------------------------\n"
                   "Get Access to Unlimited Movies on all Streaming Sites here on Telegram Instantly on Demand!\n"
                   "NB:- Both come along with private services we will upload the files right into your DM or Premium Channel (Preferably)\n"
                   "----------------------------------\n"
                   "#Action #Comedy #KDrama #18+ #Teen #Mystery #Horror etc. YOU DECIDE!\n\n"
                   "Tap on the following products below to subscribe")

        await update.message.reply_text(text=message, reply_markup=reply_markup, parse_mode="HTML")
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")


async def subscription_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if update.message is not None
    if update.message:

        message = ("You have no current Supscription")

        await update.message.reply_text(text=message)
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")


async def FAQ(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if update.message is not None
    if update.message:

        message = ("Frequently Asked Questions")

        await update.message.reply_text(text=message)
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")


async def Help_And_Support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if update.message is not None
    if update.message:

        message = ("Help and Support")

        await update.message.reply_text(text=message)
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")


async def monthly_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        query = update.callback_query
        buttons = [
            [InlineKeyboardButton("Subscribe", callback_data= "monthly_sub")], 
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        message = ("Monthly Chill - GHC 10 .00\n\n"
        "Film House Premium\n"
        "Gain Access to Unlimited Movies on Telegram Instantly! Private services included. "
        "Files uploaded to your DM or Premium Channel. #Action #Comedy #KDrama #18+ #Teen #Mystery #Horror. YOU DECIDE!\n"
        "---------------------------------------------------\n\n"
        "TERMS & CONDITIONS\n"
        "Past results do not guarantee future performance. Always ensure you're using appropriate risk management and protecting your capital.\n"
        "1. Use of stolen debit/credit cards are prohibited. You'll be caught and banned from the channel for good.\n"
        "2. Refrain from using invalid or illegitimate emails as access to the product or service will be sent to users who provide valid emails only.\n"
        "3. Disputes: Kindly refrain from issuing disputes or chargebacks. You'll be banned forever from the community/channel for good when you do so.\n"
        "4. If you have an issue with your payment, send an email to [---] or message to [---]. You'll be sorted out in due time as there's an influx of messages from many customers.\n"
        "5. Subscription on this platform is not automatic. You'd have to manually resubscribe when your current subscription has expired.\n"
        "6. Kindly do your best to contact support via the email [---] for any issues you face regarding your subscription or purchase of a service.\n"
        "7. You agree to be sent emails regarding our products/services upon purchasing our products/services.\n"
        "8. You agree that we can contact you at anytime regarding your subscription.\n"
        "9. Be sure to read the important instructions which is a pinned message on the VIP channel once you've gained access to the VIP telegram channel.\n\n"
        "PRIVACY POLICY\n"
        "We do not share your information with third parties. You may however receive information regarding forex once you make payment with our network.\n\n"
        "REFUND POLICY\n"
        "We have a 0 refund policy. We do not issue refunds for users who have successfully joined the channel.")

        await query.edit_message_text(text=message, reply_markup=reply_markup, parse_mode="HTML")
        await query.answer()
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")


async def yearly_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.callback_query:
        query = update.callback_query
        buttons = [
            [InlineKeyboardButton("Subscribe", callback_data= "yearly_sub")], 
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        message = ("Yearly Chill - GHC 100.00\n\n"
        "Film House Premium\n"
        "Gain Access to Unlimited Movies on Telegram Instantly! Private services included. "
        "Files uploaded to your DM or Premium Channel. #Action #Comedy #KDrama #18+ #Teen #Mystery #Horror. YOU DECIDE!\n"
        "---------------------------------------------------\n\n"
        "TERMS & CONDITIONS\n"
        "Past results do not guarantee future performance. Always ensure you're using appropriate risk management and protecting your capital.\n"
        "1. Use of stolen debit/credit cards are prohibited. You'll be caught and banned from the channel for good.\n"
        "2. Refrain from using invalid or illegitimate emails as access to the product or service will be sent to users who provide valid emails only.\n"
        "3. Disputes: Kindly refrain from issuing disputes or chargebacks. You'll be banned forever from the community/channel for good when you do so.\n"
        "4. If you have an issue with your payment, send an email to [---] or message to [---]. You'll be sorted out in due time as there's an influx of messages from many customers.\n"
        "5. Subscription on this platform is not automatic. You'd have to manually resubscribe when your current subscription has expired.\n"
        "6. Kindly do your best to contact support via the email [---] for any issues you face regarding your subscription or purchase of a service.\n"
        "7. You agree to be sent emails regarding our products/services upon purchasing our products/services.\n"
        "8. You agree that we can contact you at anytime regarding your subscription.\n"
        "9. Be sure to read the important instructions which is a pinned message on the VIP channel once you've gained access to the VIP telegram channel.\n\n"
        "PRIVACY POLICY\n"
        "We do not share your information with third parties. You may however receive information regarding forex once you make payment with our network.\n\n"
        "REFUND POLICY\n"
        "We have a 0 refund policy. We do not issue refunds for users who have successfully joined the channel.")

        await query.edit_message_text(text=message, reply_markup=reply_markup, parse_mode="HTML")
        await query.answer()
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")


async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await handle_payment(update, context)


#Messages
async def handle_combined_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the update contains a message and the message has text
    if update.message and update.message.text:
        text = update.message.text

         # Handling specific button texts
        if text == 'Subscription Plans':
            await subscription_plans(update, context)
        elif text == 'Subscription Status':
            await subscription_status(update, context)
        elif text == 'FAQs':
            await FAQ(update, context)
        elif text == 'Help and Support':
            await Help_And_Support(update, context)
        else:
            await update.message.reply_text("My Liege 😎! What Can We Help You With Today? Select A Command Below To Get Started 👇🏻.")
    else:
        # Handle updates without a message or text here
        print("Update does not contain a text message.")

        
async def handle_subscription_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if update.message is not None
    if update.message:
        text = update.message.text
        if text == "Monthly Chill GHC 10.00":
            await update.message.reply_text("You've selected the Monthly Chill plan. [Further instructions]")
        elif text == "Yearly Chill GHC 100.00":
            await update.message.reply_text("You've selected the Yearly Chill plan. [Further instructions]")
    else:
        # Log the issue or handle cases where update.message is None
        print("No message to reply to.")



#ERRORS
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    # Log the error or send a message to the admin here
    # The 'update' parameter is of type 'object', which can be None

    # Example: log error to console
    print(f"An error occurred: {context.error}")

    # Optionally, check if 'update' is not None and log or handle update-related errors
    if update:
        print(f"Update that caused the error: {update}")


    #MAIN FUNCTION
if __name__ == '__main__':

    print('Starting bot...')
    application = Application.builder().token(TOKEN).build()

     # Assuming 'start' is another handler you have for the '/start' command
    application.add_handler(CommandHandler("start", start))

    # Handler for selecting a subscription plan
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_subscription_selection))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_combined_text))

    application.add_handler(CallbackQueryHandler(monthly_callback, pattern='^monthly$'))
    application.add_handler(CallbackQueryHandler(yearly_callback, pattern='^yearly$'))


    # Start the bot
    application.run_polling()

    print('polling')
    application.run_polling(poll_interval=3)



