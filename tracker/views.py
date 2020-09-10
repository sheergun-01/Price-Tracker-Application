from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
from .forms import AddNewItemForm
from .models import Item

# Create your views here.
def tracker_view(request):
    items = Item.objects.order_by('-id')
    form = AddNewItemForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            url = form.cleaned_data.get('url')
            budget_price = form.cleaned_data.get('budget_price')
            crawled_data = scrape_data(url)
            Item.objects.create(
            url = url,
            title = crawled_data['title'],
            budget_price=budget_price,
            last_price=crawled_data['last_price'],
            discount_price='No Discount Yet',
            )
            return redirect('/')
        else:
            form = AddNewItemForm()
    return render(request, 'tracker/tracker.html',{'items':items,'form':form})

def scrape_data(url):
    req = Request(url,headers={'User-Agent':'Mozilla/5.0'})
    source = urlopen(req).read()
    soup = BeautifulSoup(source,'lxml')

    title = soup.find('h1', id="itemTitle").get_text().replace("Details about", "").strip()
    price = soup.find('span', id="prcIsum").get_text()
    clean_price = float(price.strip().replace("GBP", "").replace("$", ""))
    return {'title': title, 'last_price':clean_price }

