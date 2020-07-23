const doSomethingAsync = () => {
    return new Promise ((resolve, reject) => {
        (true) ? setTimeout(() => resolve('Do something Async'), 3000) : reject(new Error('Test error'))
    });
}

const doSomething = async () => {
    const something = await doSomethingAsync();
    console.log(something);
}

console.log('Before')
doSomething();
console.log('After')


const anotherFunction = async () => {
    try {
        const something = await doSomethingAsync();
        console.log(something);
    } catch(error) {
        console.log(error)
    }
}

console.log('Before_1')
anotherFunction();
console.log('After_1')