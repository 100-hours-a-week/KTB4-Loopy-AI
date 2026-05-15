import datetime

def run_planner():
    # 복습 일정을 저장할 리스트
    study_records = []
    
    # 미리 넣어두는 샘플 데이터 (프로그램 실행 시 바로 테스트해보기 위함)
    today = datetime.date.today()
    sample_topic = {
        "topic": "Pandas 데이터 전처리 핵심 메서드 백지복습",
        "learned_date": today - datetime.timedelta(days=1), # 어제 배운 것으로 가정
        "review_dates": [
            today,                                      # 1일 뒤 (오늘)
            today + datetime.timedelta(days=2),         # 3일 뒤
            today + datetime.timedelta(days=6),         # 7일 뒤
            today + datetime.timedelta(days=29)         # 30일 뒤
        ]
    }
    study_records.append(sample_topic)
    
    print("=" * 50)
    print("🧠 [아웃풋 중심 망각곡선 복습 플래너] 🧠")
    print("=" * 50)

    while True:
        print("\n=== 메인 메뉴 ===")
        print("1. 오늘 공부한 주제 추가하기")
        print("2. 💡 오늘 꼭 복습해야 할 주제 확인")
        print("3. 전체 학습 기록 및 복습 일정 보기")
        print("4. 프로그램 종료")
        
        choice = input("원하는 메뉴 번호를 입력하세요: ").strip()
        
        if choice == '1':
            topic = input("\n오늘 새롭게 학습한 주제를 입력하세요 (예: 랜덤포레스트 모델링 구현): ")
            
            # 망각곡선 주기 (1일, 3일, 7일, 30일 뒤)
            intervals = [1, 3, 7, 30]
            review_dates = [today + datetime.timedelta(days=d) for d in intervals]
            
            new_record = {
                "topic": topic,
                "learned_date": today,
                "review_dates": review_dates
            }
            study_records.append(new_record)
            
            print(f"\n✅ '{topic}'이(가) 기록되었습니다!")
            print(f"👉 첫 번째 백지 복습은 [{review_dates[0].strftime('%Y-%m-%d')}] 입니다.")
            
        elif choice == '2':
            print(f"\n📅 [오늘({today.strftime('%Y-%m-%d')})의 아웃풋 복습 리스트]")
            today_tasks = []
            
            for record in study_records:
                # 오늘 날짜가 복습 일정에 포함되어 있는지 확인
                if today in record["review_dates"]:
                    today_tasks.append(record["topic"])
            
            if today_tasks:
                for idx, task in enumerate(today_tasks, 1):
                    print(f"  {idx}. {task}")
                print("\n🔥 백지에 아웃풋을 인출해 보세요!")
            else:
                print("  오늘 복습할 내용이 없습니다. 새로운 진도를 나가거나 푹 쉬세요!")
                
        elif choice == '3':
            print("\n📚 [전체 학습 및 복습 일정]")
            if not study_records:
                print("저장된 학습 기록이 없습니다.")
            else:
                for idx, record in enumerate(study_records, 1):
                    learned = record['learned_date'].strftime('%Y-%m-%d')
                    print(f"\n{idx}. {record['topic']} (학습일: {learned})")
                    print(f"   - 1일차 복습: {record['review_dates'][0].strftime('%Y-%m-%d')}")
                    print(f"   - 3일차 복습: {record['review_dates'][1].strftime('%Y-%m-%d')}")
                    print(f"   - 7일차 복습: {record['review_dates'][2].strftime('%Y-%m-%d')}")
                    print(f"   - 30일차 복습: {record['review_dates'][3].strftime('%Y-%m-%d')}")
                    
        elif choice == '4':
            print("\n프로그램을 종료합니다. 꾸준한 아웃풋이 실력을 만듭니다! 파이팅!")
            break
            
        else:
            print("\n⚠️ 잘못된 입력입니다. 1~4 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    run_planner()
