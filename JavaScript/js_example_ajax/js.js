
console.log('Page loaded!');

const BASE_API = 'https://swapi.co/api/people';

(async () => {
    const getData = async (url) => {
        const response = await fetch(url);
        const data = await response.json()
        if (data.count > 0){
            return data;
            // return data.count;
            // return data.results[0].name;
        } else {
            // SI NO HAY DATOS REGRESA EL ERROR QUE SE PRESENTO
            throw new Error('NO SE ENCONTRO NINÚN RESULTADO...')
        }

    }
    // const peopleSW = await getData(BASE_API)
    // console.log('peopleSW -->', peopleSW);
    dropDownList = []
    try {
        const {
            results: resultArray
        } = await getData(`${BASE_API}`)
        // console.log(resultArray)
        resultArray.forEach((e, index, array) => {
            // console.log(`${index} -> ${e.name}`)
            // console.log(array)
            dropDownList.push(e.name)
        })
        
    } catch (error) {
        console.log(`A OCURRIDO UN ERROR --> ${error.message} <--`);
    }
    // console.table(dropDownList)

    const $selectNameSW = document.getElementById('nameSW');
    // $selectNameSW.options[$selectNameSW.options.length] = new Option('Text1', 'Value1');
    dropDownList.forEach(function(e, index, array){
        $selectNameSW.options[$selectNameSW.options.length] = new Option(e, index);
        // console.log(e);
    })

})()
// console.log($selectNameSW);
