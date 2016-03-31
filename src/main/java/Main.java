import org.openqa.selenium.WebDriver;
        import org.openqa.selenium.firefox.FirefoxDriver;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

/**
 * Created by Dawood-KhanM on 31/03/2016.
 */
public class Main {
    public static WebDriver driver;

    public Main OpenBrowser() throws IOException {
        System.out.println("Please be patient meanwhile Browser is opening");
        Properties prop= new Properties();
        FileInputStream fs= new FileInputStream("src/test/resources/config.properties");
        prop.load(fs);
        String url=prop.getProperty("url");
        //String browser= prop.getProperty("browser");
        driver = new FirefoxDriver();
        driver.manage().window().maximize();
        driver.manage().deleteAllCookies();
        driver.get(url);
        driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
        return this;
    }

    public void closeBrowser() {
        driver.quit();
    }

}


