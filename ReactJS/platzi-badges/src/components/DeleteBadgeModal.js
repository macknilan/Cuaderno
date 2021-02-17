import React from 'react';
/*
SE IMPORTA EL "MODAL" PARA HACER "COMPOCISION" SE LE PASA "children" A MODAL
PARA APROVECHAR EL COMPORTAMIENTO QUE MODAL TIENEPARA EXTENDERLO
*/
import Modal from './Modal';

function DeleteBadgeModal(props) {
  return (
    /* SE PASAN/RECIBEN LOS PROPS */
    <Modal isOpen={props.isOpen} onClose={props.onClose}>
      <div className="DeleteBadgeModal">
        <h1>Are You Sure?</h1>
        <p>You are about to delete this badge.</p>

        <div>
          <button onClick={props.onDeleteBadge} className="btn btn-danger mr-4">
            Delete
          </button>
          <button onClick={props.onClose} className="btn btn-primary">
            Cancel
          </button>
        </div>
      </div>
    </Modal>/* PROPS CHILDREN */
  );
}

export default DeleteBadgeModal;
