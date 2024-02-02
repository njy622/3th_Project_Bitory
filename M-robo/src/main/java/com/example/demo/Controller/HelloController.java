package com.example.demo.Controller;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
//@RestController      // @RestController = @Controller + @ResponseBody 를 합친것! 
@Controller
public class HelloController {
    @GetMapping("/home")
//    @ResponseBody   // @RestController를 쓸 때는 해당 부분 주석 달기
    public String hello() {
        return "/market/List2";
    }
    
    @GetMapping("/home4")
//    @ResponseBody   // @RestController를 쓸 때는 해당 부분 주석 달기
    public String hello2() {
    	return "/market/List3";
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
    

