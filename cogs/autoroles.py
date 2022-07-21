import nextcord
from nextcord.ext import commands

from core.auto.roles.getters import get_server_autorole_state, get_server_autorole_id


class Autorole(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if get_server_autorole_state(member.guild.id) is False:
            return
        autorole_id = get_server_autorole_id(member.guild.id)
        if welcome_channel_id == 0:
            return


def setup(client):
    client.add_cog(Autorole(client))
