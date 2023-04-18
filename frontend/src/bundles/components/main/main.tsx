import styles from './main.module.scss';

export const Main = () => {
  return (
    <div id='main' className={styles.main}>
      <div className={`${styles.content} container`}>
        <div className={styles.imagesContainer}>
          <div className={styles.imageBox}>
            <img src="https://picsum.photos/800/800?random=1" alt="" className={styles.image}/>
          </div>
          <div className={styles.imageBox}>
            <img src="https://picsum.photos/800/800?random=2" alt="" className={styles.image}/>
          </div>
          <div className={styles.imageBox}>
            <img src="https://picsum.photos/800/800?random=3" alt="" className={styles.image}/>
          </div>
          <div className={styles.imageBox}>
            <img src="https://picsum.photos/800/800?random=4" alt="" className={styles.image}/>
          </div>
        </div>
        <div className={styles.text}>
          <h1 className={styles.title}>About The Expo</h1>
          <p className={styles.description}>This year's Architecture Expo will be held at the fabulous Hong Kong City
            Hall. The Expo is constantly developing, demonstrating effective cooperation between the development market
            and the architects. This year's record-breaking edition of the Expo will feature 230 exhibitors and 25
            speakers from over 30 countries.</p>
        </div>
      </div>
    </div>
  )
    ;
}