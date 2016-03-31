import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.By;

import java.util.concurrent.TimeUnit;

/**
 * Created by Dawood-KhanM on 31/03/2016.
 */
    public class StepDefinationsLogin extends Main {
        Main obj= new Main();

        @Given("^I am on login page$")
        public void i_am_on_login_page() throws Throwable {
            obj.OpenBrowser();

        }

        @When("^I provide \"([^\"]*)\", \"([^\"]*)\"$")
        public void i_provide(String username, String password) throws Throwable {
            driver.findElement(By.id("login.userId")).sendKeys(username);
            driver.findElement(By.id("submit")).click();
            driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
            driver.findElement(By.id("login.password")).sendKeys(password);

        }

        @When("^do login$")
        public void do_login() throws Throwable {
            driver.findElement(By.id("submit")).click();
        }

        @Then("^I successfully login to GDSP Portal$")
        public void i_successfully_login_to_GDSP_Portal() throws Throwable {
            System.out.println("page validation check is in process");
            String bodyText = driver.findElement(By.id("overviewhead")).getText();

            Assert.assertTrue("User is on Home Page", bodyText.contains("Overview"));


/*
        driver.findElement(By.id("overviewhead"))
        String expectedTitle = "Title of Page";
        assertTrue(driver.getTitle().contains("Title of Page"));
        String expectedUrl= "https://m2mlobgui1.vodafone.com/GDSPGui/indexOpCo.htm";
        driver.get(expectedUrl);
        try{
            Assert.assertEquals(expectedUrl, driver.getCurrentUrl());
            System.out.println("Navigated to correct webpage");
        }
        catch(Throwable pageNavigationError){
            System.out.println("Didn't navigate to correct webpage");
        } */
        }



    }


