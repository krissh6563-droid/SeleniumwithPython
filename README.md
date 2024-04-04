# PythonSelenium Interview Questions

## Difference between findelement and findelements

Selenium WebDriver defines two methods for identifying the elements, they are findElement and findElements . findElement: This command is used to uniquely identify a web element within the web page. findElements: This command is used to uniquely identify the list of web elements within the web page.

```bash
WebElement login= driver.findElement(By.linkText("Login"));
List<WebElement> listOfElements = driver.findElements(By.xpath("//div"));
```

## Find By ID

```bash
    elementxpath = driver.findElement(By.xpath("//a[@id=’favourites’]"))
```

## Implicit wait and Explicit wait

The major difference between implicit and explicit wait is that: Implicit wait is applicable to all the elements in the test script, Explicit wait applies to the specific element only.

```bash
    driver.implicitly_wait(2)

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : revealed.is_displayed())
```

## Definitions
 ### Webdriver 
 - WebDriver is designed as a simple and more concise programming interface.
 - WebDriver is a compact object-oriented API.
 - It drives the browser effectively.

 ### Grid 
