import styles from './header.module.scss';

export const Header = () => {
  return (
    <div className={styles.header}>
      <div className={`${styles.headerContainer} container`}>
        <div className={styles.logo}>logo</div>
        <ul className={styles.navigation}>
          <li className={styles.navigationItem}>
            <a className={styles.navigationLink} href="#">Опитування</a>
          </li>
          <li className={styles.navigationItem}>
            <a className={styles.navigationLink} href="#">Функціонал</a>
          </li>
          <li className={styles.navigationItem}>
            <a className={styles.navigationLink} href="#">Передзамовлення</a>
          </li>
          <li className={styles.navigationItem}>
            <a className={styles.navigationLink} href="#">Про нас</a>
          </li>
          <li className={styles.navigationItem}>
            <a className={styles.navigationLink} href="#">Контакти</a>
          </li>
        </ul>
      </div>
    </div>
  )
    ;
}