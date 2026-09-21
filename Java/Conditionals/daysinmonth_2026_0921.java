import java.util.Scanner;

public class daysinmonth_2026_0921 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        
        String dayname;
        switch (month) {
        // switch fall-through 로 31일/30일 케이스를 묶는다.
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                dayname = "31일"; break;
            
            case 4:
            case 6:
            case 9:
            case 11:
                dayname = "30일"; break;
            
        // 2 는 28일, default 는 "잘못된 월" 출력.
            case 2: dayname = "28일"; break;
            
            default: dayname = "잘못된 월"; 
            
        }
        System.out.println(dayname);
        sc.close();
    }
}