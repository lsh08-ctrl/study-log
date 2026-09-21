import java.util.Scanner;

public class weekdayweekend_20260921 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();
        // switch fall-through 로 1~5 를 "평일"
        String name;

        switch (day) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
            name = "평일"; break;
        
        // 6~7 을 "주말" 로 묶어 출력.
        case 6:
        case 7:
            name = "주말"; break;
        
        // 그 외 "잘못된 입력"
        default:
            name = "잘못된 입력"; break;
            }
        System.out.println(name);
        sc.close();
    }
}
