from telethon import events, errors
@borg.on(events.NewMessage(incoming=True))
async def samereply(event):
	if event.is_private:
		chat_id = event.from_id
		sender = await bot.get_entity(chat_id)
		if chat_id == bot.uid:
			return
		if sender.bot:
			return
		if sender.verified:
			return
		if event.message.text:
			return await event.reply(event.message.text)
		if event.message.media:
			return await event.client.send_file(event.chat_id, event.message.media, reply_to=event.message.reply_to_msg_id)
		if event.message.document:
			return await event.client.send_file(event.chat_id, event.message.document, reply_to=event.message.reply_to_msg_id)