from django.shortcuts import render
from django.views import View
import serpapi
import matplotlib.pyplot as plt
from django.conf import settings
from resources.lang.texts import TEXTS
# Create your views here.

class TrendAdidasVsNike(View):

    def get(self, request):

        api_key = '379808e8ca161f334ee9be3ff082fb88f491d1650164f5131926c9f7ca140371'
        params_adidas = {
            'api_key':api_key,
            'engine':'google_trends',
            'q': "adidas shoes",
            'geo': 'CO',
            'cat': '18'
        }

        params_nike = {
            'api_key':api_key,
            'engine':'google_trends',
            'q': "nike shoes",
            'geo': 'CO',
            'cat': '18'
        }
        search_adidas = serpapi.search(params_adidas)
        results_adidas = search_adidas.as_dict()
        
        search_nike = serpapi.search(params_nike)
        results_nike = search_nike.as_dict()

        interest_over_time_adidas = results_adidas['interest_over_time']
        interest_over_time_nike = results_nike['interest_over_time']
    
        timeline_data_adidas = interest_over_time_adidas['timeline_data']
        timeline_data_nike = interest_over_time_nike['timeline_data']


        dates_adidas = [data['date'] for data in timeline_data_adidas]
        dates_nike = [data['date'] for data in timeline_data_nike]

        values_adidas = [data['values'][0]['value'] for data in timeline_data_adidas]
        values_nike = [data['values'][0]['value'] for data in timeline_data_nike]

        plt.plot(dates_adidas[::5], values_adidas[::5], label = 'Adidas')
        plt.plot(dates_nike[::5], values_nike[::5], label='Nike')
        plt.legend()
        plt.xlabel('Fecha')
        plt.ylabel('Interes')
        plt.title('Tendencias de Google adidas vs nike')
        plt.xticks(rotation=90)
        plt.tight_layout()


        plot_file_path = "base/static/images/plot.png" #os.path.join(settings.STATIC_URL, 'images', 'plot.png')
        print(plot_file_path)
        plt.savefig(plot_file_path)
        plt.close()

        #plt.savefig(plot_file_path_nike)

        context = {
            'urban_kicks' : TEXTS['urban_kicks'],
            'logout' : TEXTS['logout'],
            'login' : TEXTS['login'],
            'signup' : TEXTS['signup'],
            'cart_text' : TEXTS['cart'],
            'create_product' : TEXTS['create_product'],
            'create_brand' : TEXTS['create_brand'],
            'plot_file_path_adidas': plot_file_path
        }

        return render(request, 'trends.html', context)
