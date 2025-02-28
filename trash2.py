import requests

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}


data = [
    {
        "price": 200000,
        "title": "Lamborghini Aventador",
        "description": "6.5L V12, 770 к.с., 0-100 км/год за 2.8 сек.",
        "cover": "https://fox59.com/wp-content/uploads/sites/21/2018/08/s097746070.jpg?w=2505&h=1440&crop=1",
    },
    {
        "price": 300000,
        "title": "Ferrari SF90 Stradale",
        "description": "4.0L V8 гібрид, 1000 к.с., футуристичний дизайн.",
        "cover": "https://m.atcdn.co.uk/vms/media/3c4910ae62874128bc9923224a802544.jpg",
    },
    {
        "price": 180000,
        "title": "Porsche 911 Turbo S",
        "description": "3.8L бі-турбо опозитний 6-циліндровий, 650 к.с., повний привід.",
        "cover": "https://www.carviser.com/wp-content/uploads/2020/03/Porsche-Turbo-S-4-scaled.jpeg",
    },
    {
        "price": 150000,
        "title": "Audi R8 V10 Performance",
        "description": "5.2L V10, 620 к.с., атмосферний монстр.",
        "cover": "https://cdn.motor1.com/images/mgl/AlKOy/s1/2019-audi-r8-v10-performance-quattro-vegas-yellow.jpg",
    },
    {
        "price": 220000,
        "title": "McLaren 720S",
        "description": "4.0L бі-турбо V8, 720 к.с., надлегкий кузов.",
        "cover": "https://www.autocar.co.uk/sites/autocar.co.uk/files/mclaren-720s-1.jpg",
    },
    {
        "price": 350000,
        "title": "Aston Martin Valkyrie",
        "description": "6.5L V12 гібрид, 1160 к.с., натхненний Формулою-1.",
        "cover": "https://www.topgear.com/sites/default/files/2023/03/1-Aston-Martin-Valkyrie.jpg",
    },
    {
        "price": 250000,
        "title": "Mercedes-AMG GT Black Series",
        "description": "4.0L бі-турбо V8, 720 к.с., для треку.",
        "cover": "https://www.topgear.com/sites/default/files/cars-car/image/2020/09/_atf5691.jpeg",
    },
    {
        "price": 270000,
        "title": "Lexus LFA",
        "description": "4.8L V10, 560 к.с., легендарний звук двигуна.",
        "cover": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Lexus_LFA_001.JPG/1200px-Lexus_LFA_001.JPG",
    },
    {
        "price": 1300000,
        "title": "Bugatti Chiron",
        "description": "8.0L чотирьохтурбінний W16, 1500 к.с., гіперкар.",
        "cover": "https://stimg.cardekho.com/images/carexteriorimages/930x620/Bugatti/Chiron/8451/1633582433934/front-left-side-47.jpg",
    },
    {
        "price": 400000,
        "title": "Koenigsegg Jesko",
        "description": "5.0L бі-турбо V8, 1600 к.с., аеродинамічний звір.",
        "cover": "https://www.carscoops.com/wp-content/uploads/2019/04/ea5becbb-koenigsegg-jesko-.jpg",
    },
    {
        "price": 210000,
        "title": "Chevrolet Corvette Z06",
        "description": "5.5L V8 з пласким колінвалом, 670 к.с., американський спорткар.",
        "cover": "https://di-uploads-pod40.dealerinspire.com/chevroletbuickofspringvalleyinc/uploads/2023/10/2023-chevrolet-corvette-z06-driver-1-4_blog_1.webp",
    },
    {
        "price": 320000,
        "title": "Tesla Roadster",
        "description": "Електро, 1000+ к.с., 0-100 км/год за 1.9 сек.",
        "cover": "https://www.cioupdate.com.tr/wp-content/uploads/2024/03/Roadster-Tesla-ve-SpaceX.jpg",
    },
    {
        "price": 190000,
        "title": "BMW M8 Competition",
        "description": "4.4L бі-турбо V8, 625 к.с., розкіш і швидкість.",
        "cover": "https://www.topgear.com/sites/default/files/cars-car/image/2019/10/bmw_m8_coupe_fire_red_033.jpg",
    },
    {
        "price": 260000,
        "title": "Rolls-Royce Wraith",
        "description": "6.6L бі-турбо V12, 624 к.с., купе класу люкс.",
        "cover": "https://cdn.motor1.com/images/mgl/13jgw/s3/rolls-royce-black-badge-wraith-by-spofec.jpg",
    },
    {
        "price": 280000,
        "title": "Pagani Huayra",
        "description": "6.0L бі-турбо V12, 730 к.с., ручна робота.",
        "cover": "https://www.topgear.com/sites/default/files/cars-car/image/2016/08/rh_huayrabc-67.jpg",
    },
    {
        "price": 350000,
        "title": "Rimac Nevera",
        "description": "Електро, 1914 к.с., найшвидший гіперкар на батареях.",
        "cover": "https://www.electrive.com/media/2021/06/rimac-nevera-2021-02-min.png",
    },
    {
        "price": 240000,
        "title": "Ford GT",
        "description": "3.5L бі-турбо V6, 660 к.с., натхненний Ле-Маном.",
        "cover": "https://d2dsc1gf0t80gb.cloudfront.net/wp-content/uploads/2019/10/23002232/05-Ford-GT-002-1000x667.jpg",
    },
    {
        "price": 500000,
        "title": "Hennessey Venom F5",
        "description": "6.6L бі-турбо V8, 1817 к.с., неймовірна швидкість.",
        "cover": "https://www.supercars.net/blog/wp-content/uploads/2022/01/hennessey-venom-f5-feature-image.jpg",
    },
    {
        "price": 275000,
        "title": "Dodge Challenger SRT Demon 170",
        "description": "6.2L компресорний V8, 1025 к.с., найпотужніший масл-кар.",
        "cover": "https://bringatrailer.com/wp-content/uploads/2023/11/2023_dodge_challenger-srt-demon-170_demon-2-90179.jpg",
    },
    {
        "price": 330000,
        "title": "Lamborghini Huracán STO",
        "description": "5.2L V10, 640 к.с., створений для треку.",
        "cover": "https://www.goluxurys.com/wp-content/uploads/2020/11/yeni-lamborghini-huracan-sto-1.png",
    },
]

for item in data:
    response = requests.post("http://127.0.0.1:7006/cars/", headers=headers, json=item)
