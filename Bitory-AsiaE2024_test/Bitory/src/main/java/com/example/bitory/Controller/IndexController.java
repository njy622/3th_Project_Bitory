package com.example.bitory.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;



@Controller
public class IndexController {

	@GetMapping("/index")
    public String index(){

        return "index";
    }
	
	@GetMapping("/trade")
    public String market(){

        return "market/trade";
    }
	
	
}
