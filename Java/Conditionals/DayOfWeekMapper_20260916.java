import java.util.Scanner;

public class DayOfWeekMapper_20260916 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();

        // 1~7에 해당하는 요일 이름을 switch 문으로 분기
        String dayName; 
        switch (day) {
            case 1: dayName = "월요일 / Monday"; break;
            case 2: dayName = "화요일 / Tuesday"; break;
            case 3: dayName = "수요일 / Wednesday"; break;
            case 4: dayName = "목요일 / Thursday"; break;
            case 5: dayName = "금요일 / Friday"; break;
            case 6: dayName = "토요일 / Saturday"; break;
            case 7: dayName = "일요일 / Sunday"; break;
            default: dayName = "잘못된 입력"; break;
        }

        // 결과를 출력
        System.out.println(dayName);
        sc.close();
    }
}