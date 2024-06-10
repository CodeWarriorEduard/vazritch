import { Link } from 'react-router-dom';
import './Options.styles.css'


interface propsType{
  isOpen: boolean;
}


function Options({isOpen}:propsType) {
  return (
    
    <div className={isOpen? 'options-container open': 'options-container'}>
        <ul className='options-items'>
          <Link to={"https://github.com/CodeWarriorEduard/vazritch"} target='_blank'><li>REPOSITORY</li></Link>
          <Link to={"/info"}><li>DOCS</li></Link>
        </ul>
    </div>
  )
}

export default Options