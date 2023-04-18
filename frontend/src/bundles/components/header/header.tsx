import styles from './header.module.scss';

export const Header = () => {
  return (
    <div id='header' className={styles.header}>
      <div className={`${styles.headerContainer} container`}>
        <div className={styles.logo}></div>
        <ul className={styles.navigation}>
          <li className={styles.navigationItem}>
            <a href="#">Опитування</a>
          </li>
          <li className={styles.navigationItem}>
            <a href="#">Функціонал</a>
          </li>
          <li className={styles.navigationItem}>
            <a href="#">Передзамовлення</a>
          </li>
          <li className={styles.navigationItem}>
            <a href="#main">Про нас</a>
          </li>
          <li className={styles.navigationItem}>
            <a href="#footer">Контакти</a>
          </li>
        </ul>
      </div>
    </div>
  )
    ;
}