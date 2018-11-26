---
type: post
title: "Container components"
date: 2018-11-15
---

I was making a component that took in some data and produced a bar chart as a visualization.
Making the bar chart required the component to do a bit of processing on the raw data fed in,
so initially I did something like this:

```js
class FruitHarvestChart {
  initialize() {
    this.state.data = {};
  }

  processChartData() {
    const formattedData = {}; // you can mutate the object as you are not doing reassignment
    for (const fruit in Object.keys(this.state.data)) {
      formattedData[fruit] = getNumFruits(this.state.data[fruit]);
    }
  }
  
  getWidth(fruitData, numFruitsHarvested) {
    const numFruits = Object.values(fruitData).reduce((x, y) => x + y, 0);
    return numFruitsHarvested / parseFloat(numFruits);
  }

  render() {
    const data = this.processedChartData();
    return `
      <ul class="bar_chart">
        for fruit, numFruitsHarvested in data
          <li class="bar_container">
            <div class="label">{fruit}</div>
            <div class="bar" width="this.getWidth(data[fruit], numFruitsHarvested)"></div>
          </li>
      </ul>
    `;
  }
}
```

but in the end refactored it to

```js
// does all the preprocess of fruit data
class FruitHarvestChart {
  initialize() {
    this.state.data = {};
    this.barChart = new BarChart(this.processedChartData());
  }

  processChartData() {
    const formattedData = {}; // you can mutate the object as you are not doing reassignment

    let numFruits = 0;
    for (const fruit in Object.keys(this.state.data)) {
      numFruits += getNumFruits(this.state.data[fruit]);
    }

    const formattedData = {};
    for (const fruit in Object.keys(this.state.data)) {
      formattedData[fruit] = this.getWidth(this.state.data[fruit], numFruits);
    }
    return formattedData;
  }
  
  getWidth(fruitData, numFruitsHarvested) {
    const numFruits = Object.values(fruitData).reduce((x, y) => x + y, 0);
    return numFruitsHarvested / parseFloat(numFruits);
  }
  
  render() {
    return this.barChart.render();
  }
}

// generic bar chart application that can be reused
class BarChart {
  initialize(data) {
    this.state.data = data;
  }

  render() {
    return `
      <ul class="bar_chart">
        for label, width in this.state.data
          <li class="bar_container">
            <div class="label">{label}</div>
            <div class="bar" width="width"></div>
          </li>
      </ul>
    `;
  }
}
```
