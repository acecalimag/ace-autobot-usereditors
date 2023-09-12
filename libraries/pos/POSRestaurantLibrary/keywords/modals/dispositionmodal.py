import random
from datetime import timedelta
from robot.api.deco import keyword

from libraries.pos.POSRestaurantLibrary.dto.saveorderreasondetails import SaveOrderReasonDetails
from libraries.pos.POSRestaurantLibrary.locators.frame import POS_RESTAURANT_FRAME
from libraries.pos.POSRestaurantLibrary.locators.modals import dispositionmodal
from autocore.bases import WebLibraryComponent


class DispositionModalKeywords(WebLibraryComponent):

    @keyword(tags=("ModalKeywords", "DispositionModalKeywords", "SaveReasonModal"))
    def select_save_reason(self, option: str = None, action: str = 'CONTINUE',
                           _: SaveOrderReasonDetails = None) -> SaveOrderReasonDetails:
        """Select save reason.

        - ``option`` - The reason to be selected. Specify the exact text as displayed in the modal.
        --  If ``option`` does not match any reason, no reason will be selected.
        --  If not provided, a random reason will be selected.
        - ``action`` - The action to perform on the modal. Default action is to click ``CONTINUE`` button.
        Accepted values are ``CONTINUE``, ``CANCEL``, ``NO_ACTION``.

        Pre-requisite: To use this keyword, the save order modal should be displayed. See ``Click Save Order Button``.

        Returns the text in the order remark text area.
        """
        self.web.select_frame(locator=POS_RESTAURANT_FRAME)
        try:
            self.web.wait_until_visible(locator=dispositionmodal.MODAL)
            self.web.wait_until_count_is_greater_than(locator=dispositionmodal.DISPOSITIONS, count=13)

            try_count = 5
            while not self.web.is_enabled(locator=dispositionmodal.CONTINUE_BTN,
                                           timeout=timedelta(seconds=0.5)):
                if try_count == 0:
                    raise Exception(
                        "Failed to select saved reason. Tried selecting a reason but CONTINUE button is not getting enabled.")
                self.__select_save_reason(option=option)
                try_count -= 1

            details = SaveOrderReasonDetails(
                title=self.web.get_text(locator=dispositionmodal.HEADER, normalize=True),
                description=self.web.get_text(locator=dispositionmodal.DISPOSITION_LABEL),
                reasons=self.web.get_texts(locator=dispositionmodal.DISPOSITIONS),
                order_remark=self.web.get_value(locator=dispositionmodal.ORDER_REMARK_AREA)
            )

            action = action.upper().strip()
            if action == 'CONTINUE':
                self.web.click(locator=dispositionmodal.CONTINUE_BTN)
            elif action == 'CANCEL':
                self.web.click(locator=dispositionmodal.CANCEL)
            elif action == 'NO_ACTION':
                pass
            else:
                raise Exception(f"Provided action [ {action} ] is not supported.")
        except Exception as e:
            raise e
        finally:
            self.web.unselect_frame()

        self.logger.debug(details)
        return details

    def __select_save_reason(self, option: str):
        available_reasons: list[dict] = self.__get_displayed_save_reasons()
        if option is not None:
            option = option.lower().replace(" ", "")
            for i in available_reasons:
                text = i.get("text").lower().replace(" ", "")
                if option == text:
                    self.web.click(locator=f"id:{i.get('el_id')}")
                    break

        else:
            reason_id = random.choice(available_reasons).get('el_id')
            self.web.click(locator=f"id:{reason_id}")

    def __get_displayed_save_reasons(self) -> list[dict]:
        reasons_count = self.web.count(locator=dispositionmodal.DISPOSITIONS)
        details: list[dict] = []

        for i in range(1, reasons_count + 1):
            text = self.web.get_text(locator=dispositionmodal.DISPOSITIONS_INDEXED_TPL.format(i),
                                      normalize=True)
            el_id = self.web.get_attribute(locator=dispositionmodal.DISPOSITIONS_INDEXED_TPL.format(i),
                                            attribute="id")
            details.append({"text": text, "el_id": el_id})

        return details
