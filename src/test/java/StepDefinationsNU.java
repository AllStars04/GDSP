import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.openqa.selenium.By;

/**
 * Created by Dawood-KhanM on 01/04/2016.
 */
public class StepDefinationsNU extends Main{
    ManageAccount objManageAccount= new ManageAccount();

    @Given("^I am on homepage$")
    public void i_am_on_homepage() throws Throwable {
        objManageAccount.onHomepage();

    }

    @When("^I go to ManageAccount page$")
    public void i_go_to_ManageAccount_page() throws Throwable {
       objManageAccount.gotoManageAccountPage();
    }

    @When("^go to user account section$")
    public void go_to_user_account_section() throws Throwable {
       objManageAccount.goToUserAccountsPage();
    }

    @When("^I go to create new user$")
    public void i_go_to_create_new_user() throws Throwable {
        objManageAccount.goToCreateNewUser();
    }

    @Then("^I show see a page for create new user$")
    public void i_show_see_a_page_for_create_new_user() throws Throwable {
        driver.findElement(By.xpath("//h2[contains(.,'Create new User')]"));
        System.out.println("User Successfully Navigated to Create User page");
    }

}
