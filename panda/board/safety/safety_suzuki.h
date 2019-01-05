static void suzuki_rx_hook(CAN_FIFOMailBox_TypeDef *to_push) {
  // TODO
}

static int suzuki_tx_hook(CAN_FIFOMailBox_TypeDef *to_send) {
  // TODO: process samples for safety. for now just allow everything
  // 1 allows the message through
  return true;
}

static void suzuki_init(int16_t param) {
  controls_allowed = 0;   // TODO
}

const safety_hooks suzuki_hooks = {
  .init = suzuki_init,
  .rx = suzuki_rx_hook,
  .tx = suzuki_tx_hook,
  .tx_lin = nooutput_tx_lin_hook,
  .ignition = default_ign_hook,
  .fwd = nooutput_fwd_hook,
};

