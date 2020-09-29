import asab
import asab.web
import asab.web.rest
import aiohttp


class MyWebApplication(asab.Application):
    async def initialize(self):
        from asab.web import Module
        self.add_module(asab.web.Module)
        websvc = self.get_service("asab.WebService")
        container = asab.web.WebContainer(websvc, 'example:web', config={"listen": "localhost:9000"})
        container.WebApp.router.add_get("/test", self.json_test)
        container.WebApp.router.add_get("/exchange", self.exchange)

    async def json_test(self, request):
        return asab.web.rest.json_response(request=request, data={'success': True})

    async def exchange(self, request):
        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://api.exchangeratesapi.io/latest') as resp:
                if resp.status != 200:
                    return asab.web.rest.json_response(request=request, data={'success': False})
                else:
                    rates = await resp.json()
                    return asab.web.rest.json_response(request=request, data={'success': True, **rates})


if __name__ == '__main__':
    app = MyWebApplication()
    app.run()
