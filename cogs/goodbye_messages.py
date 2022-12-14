import nextcord
from nextcord.ext import commands

from core.goodbyes.getters import get_server_goodbye_channel_id, get_server_goodbye_state, \
    get_server_goodbye_message_type
from core.goodbyes.create import create_server_goodbye_embed, create_goodbye_card


class GoodbyeMessagesHandler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.bot:
            return
        if get_server_goodbye_state(member.guild.id) is False:
            return
        goodbye_channel_id = get_server_goodbye_channel_id(member.guild.id)
        if goodbye_channel_id == 0:
            return
        goodbye_channel = self.client.get_channel(goodbye_channel_id)
        message_type = get_server_goodbye_message_type(member.guild.id)
        if message_type == "embed":
            embed = create_server_goodbye_embed(member, member.guild)
            await goodbye_channel.send(embed=embed)
        elif message_type == "card":
            file = create_goodbye_card(member)
            await goodbye_channel.send(file=file)


def setup(client):
    client.add_cog(GoodbyeMessagesHandler(client))