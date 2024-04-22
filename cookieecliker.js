// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-04-15
// @description  try to take over the world!
// @author       You
// @match        https://orteil.dashnet.org/cookieclicker/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=dashnet.org
// @grant        none
// ==/UserScript==

// This is a userscript for automating the game Cookie Clicker. It should be used with a userscript manager like Tampermonkey.

// Function to click the cookie in the game
function clickCookie() {
    Game.ClickCookie();  // Uses the game's built-in method to click the cookie
}

// Function to buy the cheapest available item
function buyCheapestItem() {
    // Get all unlocked and enabled items, map them to an array of objects containing the element and its price
    const items = Array.from(document.querySelectorAll('.product.unlocked.enabled')).map(element => {
        const price = parseFloat(element.querySelector('.price').textContent.replace(',', '.'));
        return { element, price };
    }).sort((a, b) => b.price - a.price);  // Sort the items by price in descending order

    // Get the cheapest item
    const cheapestItem = items[0]?.element;
    if (cheapestItem) {
        cheapestItem.click();  // Buy the cheapest item
        console.log('buy ' + cheapestItem.querySelector('.title.productName').textContent);  // Log the purchase
    }
}

// Function to buy the cheapest available upgrade
function buyCheapestUpgrade() {
    // Get all enabled upgrades, map them to an array of objects containing the element and its price
    const upgrades = Array.from(document.querySelectorAll('#upgrades .upgrade.enabled')).map(element => {
        element.onmouseover();  // Trigger the mouseover event to show the tooltip with the price
        const price = parseFloat(document.querySelector('#tooltip').querySelector('.price').textContent.replace(',', ''));
        return { element, price };
    }).sort((a, b) => a.price - b.price);  // Sort the upgrades by price in ascending order

    // Get the cheapest upgrade
    const cheapestUpgrade = upgrades[0]?.element;
    if (cheapestUpgrade) {
        cheapestUpgrade.click();  // Buy the cheapest upgrade
        console.log('buy upgrade');  // Log the purchase
    }
}

// Main loop function
function mainLoop() {
    clickCookie();  // Click the cookie
    buyCheapestUpgrade();  // Buy the cheapest upgrade
    buyCheapestItem();  // Buy the cheapest item
}

// Start the main loop, running it every 1 millisecond
setInterval(mainLoop, 1);