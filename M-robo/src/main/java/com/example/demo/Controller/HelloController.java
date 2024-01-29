package com.example.demo.Controller;


import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.client.RestTemplate;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
//@RestController      // @RestController = @Controller + @ResponseBody 를 합친것! 
@Controller
public class HelloController {
    @GetMapping("/home")
//    @ResponseBody   // @RestController를 쓸 때는 해당 부분 주석 달기
    public String hello() {
        return "home";
    }
    
    @GetMapping("/home2")
  public String index() {
      return "index";
  }
    
    @GetMapping("/home3")
    public String main() {
    	return "main";
    }
    
    
  
        
    
   
 
}
    

