import styles from './footer.module.scss';

export const Footer = () => {
  return (
    <footer id='footer' className={styles.footer}>
      <div className={`${styles.footerContainer}`}>
        <div className={styles.company}>&copy; 2027 Your company</div>
        <div className={styles.socials}>
          <div className={styles.social}>
            <a href="#" className={styles.socialLink}></a>
          </div>
          <div className={styles.social}>
            <a href="#" className={styles.socialLink}></a>
          </div>
          <div className={styles.social}>
            <a href="#" className={styles.socialLink}></a>
          </div>
        </div>
        <a href='#header'> Back to top</a>
      </div>
    </footer>
  )
    ;
}