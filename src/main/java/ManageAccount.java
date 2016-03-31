import org.openqa.selenium.By;

import java.util.concurrent.TimeUnit;

/**
 * Created by Dawood-KhanM on 31/03/2016.
 */
public class ManageAccount extends Main {
    public void onHomepage()
    {
        driver.getCurrentUrl();
         driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);
    }
    public void gotoManageAccountPage()
    {
        driver.findElement(By.xpath("//a[contains(.,'Manage Account')]")).click();
        driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);
    }
    public void goToUserAccountsPage()
    {
        driver.findElement(By.xpath("//a[contains(@href,'details.htm')]")).click();
        driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);
    }
    public void goToCreateNewUser()
    {
        driver.findElement(By.xpath("//input[@value='Create']")).click();
        driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);
    }
}
