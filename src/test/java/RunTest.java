import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
        format = {"pretty","html:target/Dawood-html-report", "json:target/Star.json"},
        features = {"src/test/resources/Features"},
        tags = {"@login"}

)
public class RunTest {
}
