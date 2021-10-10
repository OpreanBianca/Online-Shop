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
	  onSamsungA21Load();
}

function onSamsungA21Load(){
	document.getElementById('samsungA21Description').innerHTML = products[1].description;
	document.getElementById('samsungA21Price').innerHTML = products[1].price;
	document.getElementById('samsungA21Amount').innerHTML = "Amount: " + products[1].amount;

}

function onBuyClicked(){
	document.getElementById('allShopCart').innerHTML = parseInt(document.getElementById('allShopCart').innerHTML) + 1;
	document.getElementById('allName').innerHTML = "Name: " + products[1].name;
	document.getElementById('allAmount').innerHTML = "Amount: " + document.getElementById('allShopCart').innerHTML;
}

const onFinishBuy = async () => {
	
const amountBody = {
	"id": products[1].id,
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
	  onSamsungA21Load();
}