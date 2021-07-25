$( document ).ready(getCupcakes);

async function getCupcakes() {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/cupcakes');
      cupcakes = response.data.cupcakes;
      console.log(cupcakes)
      drawCupcakes(cupcakes)
    } catch (error) {
      console.error(error);
    }
  }

function drawCupcakes(cupcakes) {
    for (cupcake of cupcakes){
        let flavor = $("<p></p>").text(`${cupcake.flavor}`);
        let rating = $("<p></p>").text(`${cupcake.rating}`);
        let size = $("<p></p>").text(`${cupcake.size}`);
        let img = $(document.createElement('img'));
        img.attr('src', cupcake.image);

        $("#cupcake-holder").append(flavor, rating, size, img);
    }
}

async function submitForm(){
    let formData = {
        "flavor": document.querySelector('#flavor').value,
        "rating": document.querySelector('#rating').value,
        "size": document.querySelector('#size').value,
        "image": document.querySelector('#image').value
    }
    drawCupcakes([formData]);
    console.log(formData);
    try {
        const response = await axios.post('http://127.0.0.1:5000/api/cupcakes', formData);
        console.log(response)
      } catch (error) {
        console.error(error);
      }
}

document.getElementById("go").addEventListener("click", function(event){
    event.preventDefault();
    submitForm();
  });