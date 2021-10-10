var products;


const getprod = async () => {
	

  const response = await fetch('http://127.0.0.1:5000/product', {
    method: 'GET',
	mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
	  'Access-Control-Allow-Origin': '*',
	  'Accept': '*/*',
	  'Connection': 'keep-alive',
    }
  });
  
	  products = await response.json();
	  onSamsungS20Load();
}

function onSamsungS20Load(){
	document.getElementById('samsungS20Description').innerHTML = products[0].description;
	document.getElementById('samsungS20Price').innerHTML = products[0].price;
	document.getElementById('samsungS20Amount').innerHTML = "Amount: " + products[0].amount;

}

function onBuyClicked(){
	document.getElementById('allShopCart').innerHTML = parseInt(document.getElementById('allShopCart').innerHTML) + 1;
	document.getElementById('allName').innerHTML = "Name: " + products[0].name;
	document.getElementById('allAmount').innerHTML = "Amount: " + document.getElementById('allShopCart').innerHTML;
}

const onFinishBuy = async () => {
	
const amountBody = {
	"id": products[0].id,
	"new_amount": parseInt(document.getElementById('allShopCart').innerHTML)
};

  const response = await fetch('http://127.0.0.1:5000/product/change_amount', {
    method: 'PUT',
	mode: 'cors',
	body: JSON.stringify(amountBody), // string or object
    headers: {
      'Content-Type': 'application/json',
	  'Access-Control-Allow-Origin': '*',
	  'Accept': '*/*',
	  'Connection': 'keep-alive',
    }
  });
  
	  products = await response.json();
	  onSamsungS20Load();
}