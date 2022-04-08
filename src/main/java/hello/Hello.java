package hello;

import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class Hello {

    @Scheduled(fixedRate = 2000)
    public void launchJob() throws Exception {
        System.out.println("cc");
    }

}
