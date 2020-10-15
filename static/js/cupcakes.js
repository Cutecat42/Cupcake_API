c = document.querySelector('.cupcakes')

async function getCupcakeInfo() {
    let res = await axios.get("/api/cupcakes");
    console.log("got", res.data);

    for (i=0;i<res.data.cupcakes.length;i++) {

        console.log(res.data.cupcakes[i])

        div = document.createElement('div');
        img = document.createElement('img')
        img.src = `${res.data.cupcakes[i].image}`;
        img.width = "200";
        c.appendChild(div);
        div.appendChild(img);
        p = document.createElement('p');
        p.innerHTML = `${res.data.cupcakes[i].flavor.toUpperCase()}: <br> 
                        Cupcake size = ${res.data.cupcakes[i].size} <br>
                        Cupcake rating = ${res.data.cupcakes[i].rating} <br>`;
        div.appendChild(p);

    }

    return res.data;
  }

getCupcakeInfo()