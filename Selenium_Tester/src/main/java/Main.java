import org.openqa.selenium.By;
import org.openqa.selenium.PageLoadStrategy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;
import java.util.Random;

public class Main {

    private static final Random random = new Random();

    private static WebElement findCategory(WebDriver driver, int number) {
        String id = "category-" + number;
        return new WebDriverWait(driver, Duration.ofSeconds(10))
                .until(ExpectedConditions.elementToBeClickable(By.id(id)));
    }

    private static void addProductToCart(WebDriver driver, WebElement product, int quantity, int returnCat) {
        WebElement h1 = product.findElement(By.tagName("h1"));
        WebElement link = h1.findElement(By.tagName("a"));
        link.click();
        WebElement quantityWanted = new WebDriverWait(driver, Duration.ofSeconds(10))
                .until(webDriver -> webDriver.findElement(By.id("quantity_wanted")));
        quantityWanted.clear();
        quantityWanted.sendKeys(Integer.toString(quantity));
        WebElement add = driver.findElement(By.className("add"));
        add.click();
        WebElement close = new WebDriverWait(driver, Duration.ofSeconds(10))
                .until(ExpectedConditions.elementToBeClickable(By.cssSelector(".btn.btn-secondary")));
        close.click();
        driver.navigate().back();
        WebElement back = findCategory(driver, returnCat);
        Actions actions = new Actions(driver);
        actions.moveToElement(back).click().build().perform();
    }

    private static void addProductsFromCategory(WebDriver driver, int category, int quantity) {
        for (int i = 0; i < quantity; i++) {
            WebElement catFirst = findCategory(driver, category);
            catFirst.click();  // wejście w kategorię

            WebElement productsRow = new WebDriverWait(driver, Duration.ofSeconds(10))
                    .until(webDriver -> webDriver.findElement(By.id("products")));

            List<WebElement> products = productsRow.findElements(By.tagName("article"));
            addProductToCart(driver, products.get(i), random.nextInt(10), category);
        }
    }

    public static void main(String[] args) {
        FirefoxOptions firefoxOptions = new FirefoxOptions();
        firefoxOptions.setPageLoadStrategy(PageLoadStrategy.EAGER);
        System.setProperty("webdriver.gecko.driver", "src/main/resources/geckodriver");

        String email = "plsf@hourly4g.site";
        String name = "Tajemniczy";
        String surname = "Klient";
        String password = "12345678";
        String birth = "2000-13-02";
        String address = "adresik 123";
        String postcode = "11-111";
        String city = "Shire";


        WebDriver driver = new FirefoxDriver(firefoxOptions);
        WebDriverWait waitDriver = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {
            driver.get("https://localhost/index.php");

            WebElement categories = waitDriver
                    .until(webDriver -> webDriver.findElement(By.id("top-menu")));
            List<WebElement> ids = categories.findElements(By.tagName("li"));

            int firstCategory = Integer.parseInt(ids.get(0).getAttribute("id").split("-")[1]);
            int secondCategory = Integer.parseInt(ids.get(1).getAttribute("id").split("-")[1]);

            addProductsFromCategory(driver, firstCategory, 5);
            addProductsFromCategory(driver, secondCategory, 5);

            WebElement cart = waitDriver
                    .until(ExpectedConditions.elementToBeClickable(By.cssSelector(".blockcart.cart-preview.active")));
            cart.click();

            waitDriver.until(ExpectedConditions.elementToBeClickable(By.cssSelector(".material-icons.pull-xs-left")));
            List<WebElement> deletes = driver.findElements(By.cssSelector(".material-icons.pull-xs-left"));

            deletes.get(0).click();

            WebElement finalization = waitDriver
                    .until(ExpectedConditions.elementToBeClickable(By.
                            cssSelector("a[href='https://localhost/index.php?controller=order']")));
            finalization.click();

            WebElement form = driver.findElement(By.id("customer-form"));
            waitDriver.until(ExpectedConditions.elementToBeClickable(form));

            WebElement gender = form.findElement(By.className("custom-radio"));
            //waitDriver.until(ExpectedConditions.elementToBeClickable(gender));
            gender.click();

            WebElement nameField = form.findElement(By.cssSelector("[name='firstname']"));
            nameField.clear();
            nameField.sendKeys(name);

            WebElement surnameField = form.findElement(By.cssSelector("[name='lastname']"));
            surnameField.clear();
            surnameField.sendKeys(surname);

            WebElement emailField = form.findElement(By.cssSelector("[name='email']"));
            emailField.clear();
            emailField.sendKeys(email);

            WebElement passwordField = form.findElement(By.cssSelector("[name='password']"));
            passwordField.clear();
            passwordField.sendKeys(password);

            WebElement accept = form.findElement(By.cssSelector("[name='psgdpr']"));
            //waitDriver.until(ExpectedConditions.elementToBeClickable(gender));
            accept.click();

            WebElement continueButton = driver.findElement(By.cssSelector("button[name='continue']"));
            continueButton.click();
            form = driver.findElement(By.className("form-fields"));
            waitDriver.until(ExpectedConditions.elementToBeClickable(form));

            WebElement addressField = form.findElement(By.cssSelector("[name='address1']"));
            addressField.clear();
            addressField.sendKeys(address);

            WebElement postcodeField = form.findElement(By.cssSelector("[name='postcode']"));
            postcodeField.clear();
            postcodeField.sendKeys(postcode);

            WebElement cityField = form.findElement(By.cssSelector("[name='city']"));
            cityField.clear();
            cityField.sendKeys(city);

            continueButton = driver.findElement(By.cssSelector("button[name='confirm-addresses']"));
            continueButton.click();

            waitDriver.until(ExpectedConditions.elementToBeClickable(//
                    driver.findElements(By.tagName("span")).stream().filter(i -> i.getText().equals("Zapłać przelewem")).findFirst().get())).click();

            WebElement agree = driver.findElement(By.id("conditions_to_approve[terms-and-conditions]"));
            agree.click();

            WebElement buy = waitDriver.until(ExpectedConditions.elementToBeClickable(//
                    driver.findElement(By.cssSelector(".btn.btn-primary.center-block"))));

            buy.click();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}